import {mkdir, copyFile} from 'node:fs/promises';
await mkdir(new URL('./assets/', import.meta.url), {recursive:true});
await copyFile(new URL('./node_modules/gsap/dist/gsap.min.js', import.meta.url), new URL('./assets/gsap.min.js', import.meta.url));
