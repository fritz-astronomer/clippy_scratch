const { build } = require('esbuild')
const pluginVue = require('esbuild-plugin-vue-next')

build({
    entryPoints: ['index.js'], // your entry file
    bundle: true,
    outfile: 'bundle.js',
    plugins: [pluginVue()]
})