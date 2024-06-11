<template>
  <form>
    <input
      id="email"
      class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
      type="email"
      placeholder="Correo electrónico"
    />
    <input
      id="password"
      class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
      type="password"
      placeholder="Contraseña"
    />
    <a href="/home">
      <button
        class="mt-5 tracking-wide font-semibold bg-red-700 text-gray-100 w-full py-4 rounded-lg hover:bg-red-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none"
      >
        <span class="material-symbols-outlined"> login </span>
        <span class="ml-3 uppercase"> Iniciar sesión </span>
      </button>
    </a>
  </form>
</template>
