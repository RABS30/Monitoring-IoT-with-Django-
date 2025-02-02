/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./dashboard/templates/dashboard/**/*.{html,js}",
    "./profileUser/templates/profileUser/**/*.{html,js}",
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      spacing: {
        '49/100' : '49%',
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

