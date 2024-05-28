<template>
<div class="max-w-md mx-auto mt-10 bg-white shadow-lg rounded-lg overflow-hidden">
    <div class="text-2xl py-4 px-6 bg-gray-900 text-white text-center font-bold uppercase">
        Registrar Usuario
    </div>
    <form class="py-4 px-6" action="" method="POST">
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="name">
                Nombre
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="name" type="text" placeholder="Ingresa tu nombre">
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="pApellido">
                Apellido Paterno
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="pApellido" type="text" placeholder="Ingresa tu primer apellido">
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="sApellido">
                Apellido Materno
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="sApellido" type="text" placeholder="Ingresa tu segundo apellido">
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="name">
                Titulo de cortesia
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="name" type="text" placeholder="Ingresa tu nombre referido">
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="nacimiento">
                Fecha de nacimiento
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="nacimiento" type="date" placeholder="Selecciona una fecha">
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="service">
                Genero
            </label>
            <select
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="service" name="service">
                <option value="">Selecciona tu genero</option>
                <option value="haircut">Masculino</option>
                <option value="coloring">Femenino</option>
                
            </select>
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="service">
                Sangre
            </label>
            <select
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="service" name="service">
                <option value="">Selecciona tu tipo de sangre</option>
                <option value="haircut">A+</option>
                <option value="coloring">B+</option>
                <option value="styling">B-</option>
                <option value="facial">O+</option>
            </select>
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="name">
                Foto
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="name" type="text" placeholder="Ingresa tu nombre referido">
        </div>

    </form>
</div>
</template> 