/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    colors: {
      'white': '#ffffff',
      "black": "#000000",
      'gray': '#f6f4f4',
      'blue': '#42D62B',
      'darkBlue': "#1FA20A",
      'lightBlue2': "#2FFD0D",
      'lightBlue': "#2AE10C",
      'textGray': "#3E3E3E",
      'red': '#FF0000',
      'actualLightBlue': '#0920F6',
      'actualLightBlue2': "#5161f3"
      // 'userColor1': "#909090"
    },
    extend: {
      keyframes: {
        shake: {
          '0%, 100%': { transform: 'translateX(0)' },
          '10%, 30%, 50%, 70%, 90%': { transform: 'translateX(-5px)' },
          '20%, 40%, 60%, 80%': { transform: 'translateX(5px)' },
        }
      },
      animation: {
        shake: 'shake 0.5s ease-in-out',
      },
    },
  },
  plugins: [],
};
