/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./*.html",
    "./business-setup/**/*.html",
    "./gst-advisory/**/*.html",
    "./corporate-governance/**/*.html",
    "./direct-tax/**/*.html",
    "./brand-protection/**/*.html",
    "./workforce-digital/**/*.html",
    "./assets/js/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'sans-serif'],
        mono: ['DM Mono', 'monospace'],
      },
      colors: {
        brand: {
          white: '#FFFFFF',
          sky: '#0284C7',
          skyLight: '#E0F2FE',
          skyHover: '#0369A1',
          slate: '#F1F5F9',
          silver: '#94A3B8',
          gold: '#D97706',
          goldLight: '#FEF3C7',
          dark: '#0F172A',
          darkAlt: '#1E293B',
        }
      }
    },
  },
  plugins: [],
};

