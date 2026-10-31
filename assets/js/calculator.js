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
    const cleanTitle = (opts.serviceTitle || 'Corporate Registration')
      .replace(/-/g, ' ')
      .replace(/\b\w/g, l => l.toUpperCase());

    // State options
    const stateOptions = Object.keys(STAMP_DUTY_RULES)
      .filter(k => k !== '_default')
      .sort()
      .map(s => `<option value="${s}" ${s === 'Kerala' ? 'selected' : ''}>${s}</option>`)
      .join('');

    // Capital slab options
    const slabOptions = CAPITAL_SLABS
      .map(s => `<option value="${s.value}" ${s.value === 1000000 ? 'selected' : ''}>${s.label}</option>`)
      .join('');

    return `
<div class="bg-white rounded-2xl p-6 sm:p-8 border border-slate-200 shadow-sm" role="region" aria-label="Fee Calculator">
  <div class="flex items-center gap-3 mb-6">
    <div class="w-10 h-10 rounded-xl bg-brand-skyLight text-brand-sky flex items-center justify-center font-bold text-lg shadow-sm">
      ₹
    </div>
    <div>
      <h3 class="text-lg font-extrabold text-brand-dark">Statutory Fee Calculator</h3>
      <p class="text-xs text-slate-500">${cleanTitle}</p>
    </div>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
    <div>
      <label class="block text-xs font-bold uppercase text-slate-700 mb-1" for="calc-state">State of Registration</label>
      <select id="calc-state" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition-all shadow-sm cursor-pointer" name="calc_state" aria-label="Select state">
        ${stateOptions}
      </select>
    </div>

    <div>
      <label class="block text-xs font-bold uppercase text-slate-700 mb-1" for="calc-capital">Authorized Capital</label>
      <select id="calc-capital" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-brand-sky focus:bg-white focus:outline-none transition-all shadow-sm cursor-pointer" name="calc_capital" aria-label="Select authorized capital">
        ${slabOptions}
      </select>
    </div>
  </div>

  <!-- Dynamic stat cards -->
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center pt-4 border-t border-slate-200">
    <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
      <span class="block text-[10px] uppercase font-bold text-slate-500">Professional Fee</span>
      <span id="calc-prof-val" class="font-black text-sm text-brand-dark mt-1 block">${formatCurrency(opts.baseFee)}</span>
    </div>
    <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
      <span class="block text-[10px] uppercase font-bold text-slate-500">State Stamp Duty</span>
      <span id="calc-stamp-val" class="font-black text-sm text-brand-gold mt-1 block">₹5,000</span>
    </div>
    <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
      <span class="block text-[10px] uppercase font-bold text-slate-500">GST (18%)</span>
      <span id="calc-gst-val" class="font-black text-sm text-brand-dark mt-1 block">${formatCurrency(Math.round(opts.baseFee * GST_RATE))}</span>
    </div>
    <div class="p-3 bg-brand-skyLight rounded-xl border border-brand-sky/30">
      <span class="block text-[10px] uppercase font-bold text-brand-sky">Estimated Total</span>
      <span id="calc-total-val" class="font-black text-sm text-brand-dark mt-1 block">${formatCurrency(Math.round(opts.baseFee * (1 + GST_RATE)))}</span>
    </div>
  </div>

  <!-- Detailed formula breakdown -->
  <div id="calc-result" class="mt-4 p-3.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 leading-relaxed">
    Select your state above to compute dynamic statutory stamp duty.
  </div>

  <!-- CTA Buttons -->
  <div class="mt-6 flex flex-wrap items-center gap-3">
    <a
      href="#inquiry"
      class="bg-brand-sky hover:bg-brand-skyHover text-white font-bold text-xs px-5 py-2.5 rounded-lg shadow transition"
      id="calc-cta"
      data-service-id="${opts.serviceId}"
    >
      Get a Free Quote &rarr;
    </a>
    <a
      href="https://wa.me/918606918247?text=${encodeURIComponent('Hi CraftEgon! I want a statutory fee quote for ' + cleanTitle + '.')}"
      target="_blank"
      rel="noopener noreferrer"
      class="inline-flex items-center gap-2 bg-[#25D366]/10 border border-[#25D366]/40 text-[#128C7E] hover:bg-[#25D366]/20 font-bold text-xs px-4 py-2.5 rounded-lg transition"
    >
      <span>💬 Ask on WhatsApp</span>
    </a>
  </div>

  <!-- Statutory Disclaimer -->
  <div class="mt-6 p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-800 text-xs flex items-center gap-2.5">
    <span class="text-base shrink-0">ℹ️</span>
    <p class="leading-relaxed">
      Estimates are indicative. Stamp duty rates are subject to change per state government notifications.
      Government fees are charged at actuals. Final invoice will reflect current applicable rates.
    </p>
  </div>
</div>
    `;
  }
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
    const stampEl   = container.querySelector('#calc-stamp-val');
    const gstEl     = container.querySelector('#calc-gst-val');
    const totalEl   = container.querySelector('#calc-total-val');

    if (!stateEl || !capitalEl) return;

    const state   = stateEl.value;
    const capital = parseInt(capitalEl.value, 10);

    if (!state) {
      if (resultEl) resultEl.innerHTML = `<span class="text-slate-500 font-medium">← Please select your state of registration above to calculate stamp duty.</span>`;
      if (stampEl) stampEl.textContent = '₹0';
      if (totalEl) totalEl.textContent = formatCurrency(Math.round(baseFee * (1 + GST_RATE)));
      return;
    }

    const fee = calculateTotalFee(baseFee, state, capital);

    if (stampEl) stampEl.textContent = formatCurrency(fee.stamp_duty);
    if (gstEl) gstEl.textContent = formatCurrency(fee.gst_amount);
    if (totalEl) totalEl.textContent = formatCurrency(fee.total);

    if (resultEl) {
      resultEl.innerHTML = `
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div><strong class="text-brand-dark font-semibold">Statutory Formula (${state} · ${_getLabelForValue(capital)}):</strong></div>
          <div class="font-mono text-slate-700">
            ${formatCurrency(fee.professional_fee)} (Prof) + ${formatCurrency(fee.stamp_duty)} (Stamp Duty) + ${formatCurrency(fee.gst_amount)} (GST 18%) + ${formatCurrency(fee.govt_fees)} (MCA ROC) = <strong class="text-brand-dark">${formatCurrency(fee.total)}</strong>
          </div>
        </div>
      `;
    }

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

    elements.forEach((el, idx) => {
      // If the container already has pre-rendered inputs, don't destroy it!
      if (el.querySelector('#prod-calc-state') || el.querySelector('#calc-state-select') || el.dataset.calcReady === 'true') {
        return;
      }

      if (!el.id) el.id = `ccs-calculator-${idx}`;

      const serviceId = el.dataset.ccsCalculator || '';
      const baseFee = parseInt(el.dataset.baseFee, 10) || 7999;
      const title = el.dataset.serviceTitle || serviceId || 'Corporate Service';

      initCalculator(el.id, {
        baseFee: baseFee,
        serviceTitle: title,
        serviceId: serviceId,
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

if (typeof window !== 'undefined') {
  window.CCSCalculator = CCSCalculator;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CCSCalculator;
}

/* ── Auto-init on DOM ready ───────────────────────────────── */
(function () {
  function _run() {
    const elements = document.querySelectorAll('[data-ccs-calculator]');
    if (!elements.length) return;

    elements.forEach((el, idx) => {
      // If the container already has pre-rendered inputs, do not overwrite it!
      if (el.querySelector('#prod-calc-state') || el.querySelector('#calc-state-select') || el.dataset.calcReady === 'true') {
        return;
      }

      if (!el.id) el.id = `ccs-calculator-auto-${idx}`;
      const serviceId = el.dataset.ccsCalculator || '';
      let baseFee     = parseInt(el.dataset.baseFee, 10) || 7999;
      let title       = el.dataset.serviceTitle || serviceId || 'Corporate Service';

      CCSCalculator.initCalculator(el.id, { baseFee, serviceTitle: title, serviceId });
    });
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', _run);
    } else {
      _run();
    }
  }
})();
