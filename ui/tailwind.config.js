/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#0052cc',
          light: '#2684ff',
          dark: '#003d99',
        }
      }
    },
  },
  plugins: [],
}
