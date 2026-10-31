/**
 * CraftEgon Corporate Services — Application Configuration
 * ========================================================
 * Global runtime settings, webhook endpoints, and CRM integration parameters.
 *
 * @version 2.0.0
 */

(function () {
    'use strict';

    window.CCS_CONFIG = window.CCS_CONFIG || {
        // Platform Information
        platformName: 'CraftEgon Corporate Services',
        canonicalOrigin: 'https://corporateservices.craftegon.com',

        // Contact & Telephony
        phoneHelpline: '+918606918247',
        phoneDisplay: '+91 86069 18247',
        whatsAppNumber: '918606918247',
        defaultWhatsAppMsg: 'Hi Craftegon, I need assistance with corporate compliance.',

        // Lead Intake & Webhook Dispatcher
        // Configurable endpoint for CRM/Slack/Discord/Zapier/Webhook delivery
        webhookUrl: window.CCS_WEBHOOK_URL || '/api/lead-capture',
        webhookTimeoutMs: 6000,
        enableLocalStorageBackup: true,
        localStorageKey: 'ccs_lead_intakes',

        // SLA & Performance
        callbackPromiseMinutes: 10,
        enableDebugLogging: false
    };
})();
