/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html, ts}"],
  theme: {
    extend: {
      colors: {
        background: "rgba(var(--background))",
        background_accent: "rgba(var(--background_accent))",

        primary: "rgba(var(--primary))",
        secondary: "rgba(var(--secondary))",
      },
    },
  },
  plugins: [],
};
