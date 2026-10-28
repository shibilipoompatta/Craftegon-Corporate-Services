/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./*.html",
    "./**/*.html",
    "./assets/js/**/*.js",
    "./build_*.py"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Plus Jakarta Sans', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
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
