/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    colors: {
      'white': '#ffffff',
      "black": "#000000",
      'gray': '#f6f4f4',
      'blue': '#8B008B',
      'darkBlue': "#800080",
      'lightBlue2': "#6A0DAD",
      'lightBlue': "#ae00cc",
      'textGray': "#3E3E3E",
      'red': '#FF0000',
      // 'userColor1': "#909090"
    },
    extend: {
      spacing: {
        '128': '32rem',
      },
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
