/**
 * CraftEgon Corporate Services — Fee Calculator Engine
 * =====================================================
 * Dynamic stamp duty + professional fee calculator.
 * Supports 10+ major Indian states with realistic slab rules.
 *
 * Usage:
 *  CCSCalculator.initCalculator('my-container-id');
 *  // or via HTML: <div data-ccs-calculator="pvt-ltd-registration"></div>
 *
 * @module CCSCalculator
 * @version 1.0.0
 */

'use strict';

/* ============================================================
   STAMP_DUTY_RULES
   Structure: { [stateName]: (authorizedCapital) => stampDutyAmount }
   All amounts in Indian Rupees (INR).
   Sources: State-specific Stamp Act schedules (indicative rates).
   ============================================================ */
const STAMP_DUTY_RULES = {

  /**
   * Maharashtra — Companies Act / Bombay Stamp Act
   * Progressive slabs on Authorized Capital
   */
  'Maharashtra': function (capital) {
    if (capital <= 100000)    return 200;
    if (capital <= 500000)    return 1000;
    if (capital <= 1000000)   return 2000;
    if (capital <= 2500000)   return 4000;
    if (capital <= 5000000)   return 7500;
    if (capital <= 10000000)  return 12000;
    if (capital <= 50000000)  return 50000;
    if (capital <= 100000000) return 100000;
    return 200000; // > 10 Cr
  },

  /**
   * Delhi — NCT of Delhi Stamp (Prevention of Undervaluation) Rules
   * Relatively flat, lower than most states
   */
  'Delhi': function (capital) {
    if (capital <= 100000)    return 200;
    if (capital <= 500000)    return 400;
    if (capital <= 1000000)   return 800;
    if (capital <= 2500000)   return 1500;
    if (capital <= 5000000)   return 2500;
    if (capital <= 10000000)  return 4000;
    if (capital <= 50000000)  return 15000;
    if (capital <= 100000000) return 25000;
    return 50000; // > 10 Cr
  },

  /**
   * Karnataka — Karnataka Stamp Act
   */
  'Karnataka': function (capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 2000;
    if (capital <= 1000000)   return 3500;
    if (capital <= 2500000)   return 6000;
    if (capital <= 5000000)   return 10000;
    if (capital <= 10000000)  return 15000;
    if (capital <= 50000000)  return 60000;
    if (capital <= 100000000) return 100000;
    return 200000;
  },

  /**
   * Kerala — Kerala Stamp Act (Schedule I)
   */
  'Kerala': function (capital) {
    if (capital <= 100000)    return 1000;
    if (capital <= 500000)    return 3000;
    if (capital <= 1000000)   return 5000;
    if (capital <= 2500000)   return 8000;
    if (capital <= 5000000)   return 12000;
    if (capital <= 10000000)  return 18000;
    if (capital <= 50000000)  return 50000;
    if (capital <= 100000000) return 80000;
    return 150000;
  },

  /**
   * Tamil Nadu — Tamil Nadu Stamp Act
   */
  'Tamil Nadu': function (capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 1500;
    if (capital <= 1000000)   return 3000;
    if (capital <= 2500000)   return 5000;
    if (capital <= 5000000)   return 8500;
    if (capital <= 10000000)  return 13000;
    if (capital <= 50000000)  return 45000;
    if (capital <= 100000000) return 75000;
    return 150000;
  },

  /**
   * Gujarat — Gujarat Stamp Act
   */
  'Gujarat': function (capital) {
    if (capital <= 100000)    return 1000;
    if (capital <= 500000)    return 2500;
    if (capital <= 1000000)   return 4000;
    if (capital <= 2500000)   return 7000;
    if (capital <= 5000000)   return 11000;
    if (capital <= 10000000)  return 17000;
    if (capital <= 50000000)  return 55000;
    if (capital <= 100000000) return 90000;
    return 175000;
  },

  /**
   * Rajasthan — Rajasthan Stamp Act
   */
  'Rajasthan': function (capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 2000;
    if (capital <= 1000000)   return 3500;
    if (capital <= 2500000)   return 6000;
    if (capital <= 5000000)   return 10000;
    if (capital <= 10000000)  return 15000;
    if (capital <= 50000000)  return 50000;
    if (capital <= 100000000) return 80000;
    return 160000;
  },

  /**
   * Uttar Pradesh — U.P. Stamp Act
   */
  'Uttar Pradesh': function (capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 1500;
    if (capital <= 1000000)   return 2500;
    if (capital <= 2500000)   return 4500;
    if (capital <= 5000000)   return 7500;
    if (capital <= 10000000)  return 12000;
    if (capital <= 50000000)  return 40000;
    if (capital <= 100000000) return 70000;
    return 130000;
  },

  /**
   * West Bengal — West Bengal Stamp Act
   */
  'West Bengal': function (capital) {
    if (capital <= 100000)    return 300;
    if (capital <= 500000)    return 1000;
    if (capital <= 1000000)   return 2000;
    if (capital <= 2500000)   return 3500;
    if (capital <= 5000000)   return 6000;
    if (capital <= 10000000)  return 10000;
    if (capital <= 50000000)  return 35000;
    if (capital <= 100000000) return 60000;
    return 110000;
  },

  /**
   * Telangana — Telangana Stamp Act
   */
  'Telangana': function (capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 1500;
    if (capital <= 1000000)   return 3000;
    if (capital <= 2500000)   return 5500;
    if (capital <= 5000000)   return 9000;
    if (capital <= 10000000)  return 14000;
    if (capital <= 50000000)  return 48000;
    if (capital <= 100000000) return 78000;
    return 150000;
  },

  /**
   * Punjab — Punjab Stamp Act
   */
  'Punjab': function (capital) {
    if (capital <= 100000)    return 400;
    if (capital <= 500000)    return 1200;
    if (capital <= 1000000)   return 2200;
    if (capital <= 2500000)   return 4000;
    if (capital <= 5000000)   return 7000;
    if (capital <= 10000000)  return 11000;
    if (capital <= 50000000)  return 38000;
    if (capital <= 100000000) return 65000;
    return 120000;
  },

  /**
   * Haryana — Haryana Stamp Act
   */
  'Haryana': function (capital) {
    if (capital <= 100000)    return 400;
    if (capital <= 500000)    return 1200;
    if (capital <= 1000000)   return 2200;
    if (capital <= 2500000)   return 4000;
    if (capital <= 5000000)   return 6500;
    if (capital <= 10000000)  return 10500;
    if (capital <= 50000000)  return 36000;
    if (capital <= 100000000) return 60000;
    return 115000;
  },

  /**
   * Default fallback — for states without specific rules
   */
  '_default': function (capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 1500;
    if (capital <= 1000000)   return 3000;
    if (capital <= 2500000)   return 5000;
    if (capital <= 5000000)   return 8000;
    if (capital <= 10000000)  return 13000;
    if (capital <= 50000000)  return 45000;
    if (capital <= 100000000) return 75000;
    return 150000;
  },
};

/* ── Capital Slabs ────────────────────────────────────────── */

/**
 * Standard authorized capital slabs used in the calculator dropdown.
 * @type {Array<{label: string, value: number}>}
 */
const CAPITAL_SLABS = [
  { label: '₹1 Lakh  (Minimum)',    value: 100000    },
  { label: '₹5 Lakhs',              value: 500000    },
  { label: '₹10 Lakhs',             value: 1000000   },
  { label: '₹25 Lakhs',             value: 2500000   },
  { label: '₹50 Lakhs',             value: 5000000   },
  { label: '₹1 Crore',              value: 10000000  },
  { label: '₹5 Crores',             value: 50000000  },
  { label: '₹10 Crores',            value: 100000000 },
  { label: '₹10 Crores+',           value: 100000001 },
];

/* ── GST Rate ─────────────────────────────────────────────── */
const GST_RATE = 0.18; // 18% on professional fee

/* ============================================================
   CCSCalculator Namespace
   ============================================================ */
const CCSCalculator = (function () {

  /* ── Service registry (loaded from /data/services.json) ── */
  let _serviceRegistry = {};

  /* ── formatCurrency ───────────────────────────────────────── */

  /**
   * Formats a number as Indian currency string (₹1,00,000).
   * @param {number} amount
   * @returns {string}
   */
  function formatCurrency(amount) {
    if (isNaN(amount) || amount == null) return '₹0';
    const rounded = Math.round(amount);
    // Indian numbering system
    const str = rounded.toString();
    let result = '';
    const len = str.length;

    if (len <= 3) {
      result = str;
    } else {
      // Last 3 digits
      result = ',' + str.slice(len - 3);
      // Remaining digits in groups of 2
      const rest = str.slice(0, len - 3);
      for (let i = rest.length; i > 0; i -= 2) {
        result = ',' + rest.slice(Math.max(0, i - 2), i) + result;
      }
      result = result.replace(/^,/, '');
    }

    return '₹' + result;
  }

  /* ── calculateStampDuty ───────────────────────────────────── */

  /**
   * Returns stamp duty for a given state and authorized capital.
   * Falls back to _default if state not found.
   * @param {string} state
   * @param {number} authorizedCapital
   * @returns {number}
   */
  function calculateStampDuty(state, authorizedCapital) {
    const ruleFn = STAMP_DUTY_RULES[state] || STAMP_DUTY_RULES['_default'];
    return ruleFn(authorizedCapital);
  }

  /* ── calculateTotalFee ────────────────────────────────────── */

  /**
   * Computes the complete fee breakdown.
   * @param {number} baseFee          Professional fee (excl. GST)
   * @param {string} state            Selected Indian state
   * @param {number} authorizedCapital  In INR
   * @returns {{
   *   professional_fee: number,
   *   stamp_duty: number,
   *   gst_amount: number,
   *   govt_fees: number,
   *   total: number,
   *   breakdown: string
   * }}
   */
  function calculateTotalFee(baseFee, state, authorizedCapital) {
    const professional_fee = baseFee;
    const stamp_duty       = calculateStampDuty(state, authorizedCapital);
    const gst_amount       = Math.round(professional_fee * GST_RATE);

    // MCA2 registration govt fee (ROC filing fees — indicative)
    const govt_fees        = _estimateGovtFees(authorizedCapital);

    const total = professional_fee + stamp_duty + gst_amount + govt_fees;

    const breakdown =
      `Professional Fee: ${formatCurrency(professional_fee)} + ` +
      `Stamp Duty (${state}): ${formatCurrency(stamp_duty)} + ` +
      `Govt. Fees: ${formatCurrency(govt_fees)} + ` +
      `GST @18%: ${formatCurrency(gst_amount)} = ` +
      `Total: ${formatCurrency(total)}`;

    return { professional_fee, stamp_duty, gst_amount, govt_fees, total, breakdown };
  }

  /**
   * Estimates MCA2 ROC filing fees based on authorized capital.
   * These are government-prescribed fees and do not attract GST.
   * @param {number} capital
   * @returns {number}
   * @private
   */
  function _estimateGovtFees(capital) {
    if (capital <= 100000)    return 500;
    if (capital <= 500000)    return 2000;
    if (capital <= 1000000)   return 4000;
    if (capital <= 5000000)   return 8000;
    if (capital <= 10000000)  return 15000;
    if (capital <= 50000000)  return 30000;
    if (capital <= 100000000) return 50000;
    return 75000;
  }

  /* ── initCalculator ───────────────────────────────────────── */

  /**
   * Builds the interactive calculator UI inside a DOM container.
   * @param {string} containerId   ID of the target <div>
   * @param {Object} [opts]
   * @param {number} [opts.baseFee=4999]     Default professional fee
   * @param {string} [opts.serviceTitle='Company Registration'] Service label
   * @param {string} [opts.serviceId='']     Service ID for the lead form
   */
  function initCalculator(containerId, opts = {}) {
    const container = document.getElementById(containerId);
    if (!container) {
      console.warn(`[CCSCalculator] Container #${containerId} not found.`);
      return;
    }

    const defaults = {
      baseFee:      opts.baseFee      || 4999,
      serviceTitle: opts.serviceTitle || 'Company Registration',
      serviceId:    opts.serviceId    || '',
    };

    // Render HTML scaffold
    container.innerHTML = _buildCalculatorHTML(defaults);

    // Bind events
    _bindCalculatorEvents(container, defaults);

    // Run initial calculation
    _runCalculation(container, defaults.baseFee);

    console.log(`[CCSCalculator] Initialised in #${containerId} for "${defaults.serviceTitle}"`);
  }

  /**
   * Generates the calculator widget HTML.
   * @private
   */
  function _buildCalculatorHTML(opts) {
    // State options
    const stateOptions = Object.keys(STAMP_DUTY_RULES)
      .filter(k => k !== '_default')
      .sort()
      .map(s => `<option value="${s}">${s}</option>`)
      .join('');

    // Capital slab options
    const slabOptions = CAPITAL_SLABS
      .map(s => `<option value="${s.value}">${s.label}</option>`)
      .join('');

    return `
<div class="calculator-widget" role="region" aria-label="Fee Calculator">
  <h3 class="calc-title">
    <span class="text-gold">₹</span> Fee Calculator — ${opts.serviceTitle}
  </h3>

  <div class="grid-2" style="gap:1rem; margin-bottom:1.5rem;">
    <div class="form-group">
      <label class="form-label" for="calc-state">State of Registration</label>
      <select id="calc-state" class="form-select" name="calc_state" aria-label="Select state">
        <option value="">— Select State —</option>
        ${stateOptions}
      </select>
    </div>

    <div class="form-group">
      <label class="form-label" for="calc-capital">Authorized Capital</label>
      <select id="calc-capital" class="form-select" name="calc_capital" aria-label="Select authorized capital">
        ${slabOptions}
      </select>
    </div>
  </div>

  <!-- Base fee display -->
  <div class="flex items-center gap-4 mb-6 p-4 rounded-lg"
       style="background:var(--color-gold-muted); border:1px solid rgba(197,160,89,0.25);">
    <span class="text-sm font-semibold" style="color:var(--color-text);">Professional Fee (excl. GST):</span>
    <span class="text-mono font-bold text-gold text-lg"
          id="calc-base-fee">${formatCurrency(opts.baseFee)}</span>
    <span class="badge badge-gold">Inclusive of Consultation</span>
  </div>

  <!-- Dynamic breakdown -->
  <div class="calc-result-card" id="calc-result" aria-live="polite" aria-atomic="true">
    <p class="text-xs text-muted mb-4" style="color:rgba(248,249,246,0.5);">
      Select your state to see the full fee breakdown.
    </p>
  </div>

  <!-- CTA -->
  <div class="flex flex-wrap gap-4 mt-6">
    <a
      href="#enquiry-form"
      class="btn btn-primary"
      id="calc-cta"
      data-service-id="${opts.serviceId}"
      aria-label="Get a quote for ${opts.serviceTitle}"
    >
      Get a Free Quote
    </a>
    <a
      href="https://wa.me/919995204905?text=${encodeURIComponent('Hi CraftEgon! I want a quote for ' + opts.serviceTitle + '.')}"
      target="_blank"
      rel="noopener noreferrer"
      class="btn btn-whatsapp btn-sm"
    >
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
      </svg>
      Ask on WhatsApp
    </a>
  </div>

  <!-- Disclaimer -->
  <div class="disclaimer-badge gold mt-6">
    <span class="disclaimer-icon">ℹ️</span>
    <p>
      Estimates are indicative. Stamp duty rates are subject to change per state government notifications.
      Government fees are charged at actuals. Final invoice will reflect current applicable rates.
    </p>
  </div>
</div>
    `;
  }

  /**
   * Binds change events on the state and capital dropdowns.
   * @private
   */
  function _bindCalculatorEvents(container, opts) {
    const stateSelect   = container.querySelector('#calc-state');
    const capitalSelect = container.querySelector('#calc-capital');

    if (stateSelect)   stateSelect.addEventListener('change',   () => _runCalculation(container, opts.baseFee));
    if (capitalSelect) capitalSelect.addEventListener('change', () => _runCalculation(container, opts.baseFee));
  }

  /* ── updateCalculation / _runCalculation ─────────────────── */

  /**
   * Public alias — re-runs the calculation for an already-mounted widget.
   * @param {string} containerId
   * @param {number} baseFee
   */
  function updateCalculation(containerId, baseFee) {
    const container = document.getElementById(containerId);
    if (container) _runCalculation(container, baseFee);
  }

  /**
   * Reads current dropdown values, computes fees, updates the result card.
   * @param {HTMLElement} container
   * @param {number} baseFee
   * @private
   */
  function _runCalculation(container, baseFee) {
    const stateEl   = container.querySelector('#calc-state');
    const capitalEl = container.querySelector('#calc-capital');
    const resultEl  = container.querySelector('#calc-result');

    if (!stateEl || !capitalEl || !resultEl) return;

    const state   = stateEl.value;
    const capital = parseInt(capitalEl.value, 10);

    if (!state) {
      resultEl.innerHTML = `
        <p class="text-xs" style="color:rgba(248,249,246,0.5);">
          ← Select your state to calculate stamp duty.
        </p>`;
      return;
    }

    const fee = calculateTotalFee(baseFee, state, capital);

    resultEl.innerHTML = `
      <p class="text-xs mb-4" style="color:rgba(248,249,246,0.45); letter-spacing:0.08em; text-transform:uppercase; font-family:var(--font-mono);">
        Fee Breakdown — ${state}
      </p>

      <div class="calc-breakdown-row">
        <span class="calc-label">Professional Fee</span>
        <span class="calc-value">${formatCurrency(fee.professional_fee)}</span>
      </div>

      <div class="calc-breakdown-row">
        <span class="calc-label">GST @ 18%</span>
        <span class="calc-value">${formatCurrency(fee.gst_amount)}</span>
      </div>

      <div class="calc-breakdown-row">
        <span class="calc-label">Stamp Duty (${state})</span>
        <span class="calc-value">${formatCurrency(fee.stamp_duty)}</span>
      </div>

      <div class="calc-breakdown-row">
        <span class="calc-label">Govt. Filing Fees (MCA)</span>
        <span class="calc-value">${formatCurrency(fee.govt_fees)}</span>
      </div>

      <div class="calc-breakdown-row total-row">
        <span class="calc-label">Estimated Total</span>
        <span class="calc-value">${formatCurrency(fee.total)}</span>
      </div>

      <p class="mt-4 text-xs" style="color:rgba(248,249,246,0.35); line-height:1.6;">
        Capital: ${_getLabelForValue(capital)} &nbsp;·&nbsp; Stamp duty at ${state} rates.
      </p>
    `;

    console.log('[CCSCalculator] Calculation:', fee.breakdown);
  }

  /**
   * Returns the human-readable label for a capital slab value.
   * @param {number} value
   * @returns {string}
   * @private
   */
  function _getLabelForValue(value) {
    const slab = CAPITAL_SLABS.find(s => s.value === value);
    return slab ? slab.label : formatCurrency(value);
  }

  /* ── Auto-init from data attributes ──────────────────────── */

  /**
   * Scans the DOM for [data-ccs-calculator] elements and initialises each.
   * Fetches service base fees from /data/services.json if available.
   */
  async function _autoInit() {
    const elements = document.querySelectorAll('[data-ccs-calculator]');
    if (elements.length === 0) return;

    console.log(`[CCSCalculator] Auto-init — found ${elements.length} calculator element(s).`);

    // Attempt to load service registry
    try {
      const res = await fetch('/data/services.json');
      if (res.ok) {
        _serviceRegistry = await res.json();
        console.log('[CCSCalculator] Service registry loaded:', Object.keys(_serviceRegistry).length, 'services.');
      }
    } catch (err) {
      console.warn('[CCSCalculator] Could not load /data/services.json — using defaults.', err.message);
    }

    elements.forEach((el, idx) => {
      // Ensure the element has an ID
      if (!el.id) el.id = `ccs-calculator-${idx}`;

      const serviceId = el.dataset.ccsCalculator || '';
      const service   = _serviceRegistry[serviceId] || {};

      initCalculator(el.id, {
        baseFee:      service.base_fee      || el.dataset.baseFee      || 4999,
        serviceTitle: service.title         || el.dataset.serviceTitle || serviceId || 'Service',
        serviceId:    serviceId,
      });
    });
  }

  /* ── Public API ───────────────────────────────────────────── */
  return {
    initCalculator,
    updateCalculation,
    calculateStampDuty,
    calculateTotalFee,
    formatCurrency,
    STAMP_DUTY_RULES,
    CAPITAL_SLABS,
  };

})();

/* ── Auto-init on DOM ready ───────────────────────────────── */
(function () {
  function _run() {
    // Re-use the private _autoInit exposed via closure trick
    // We trigger the same scanning logic by exposing a public init method
    const elements = document.querySelectorAll('[data-ccs-calculator]');
    if (!elements.length) return;

    elements.forEach(async (el, idx) => {
      if (!el.id) el.id = `ccs-calculator-auto-${idx}`;
      const serviceId = el.dataset.ccsCalculator || '';
      let baseFee     = parseInt(el.dataset.baseFee, 10) || 4999;
      let title       = el.dataset.serviceTitle || serviceId || 'Service';

      // Try to hydrate from services.json
      try {
        const res = await fetch('/data/services.json');
        if (res.ok) {
          const registry = await res.json();
          if (registry[serviceId]) {
            baseFee = registry[serviceId].base_fee || baseFee;
            title   = registry[serviceId].title    || title;
          }
        }
      } catch (_) { /* silent — use defaults */ }

      CCSCalculator.initCalculator(el.id, { baseFee, serviceTitle: title, serviceId });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', _run);
  } else {
    _run();
  }
})();
