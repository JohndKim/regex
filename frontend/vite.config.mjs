import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tsconfigPaths from 'vite-tsconfig-paths';

// export default defineConfig({
//   plugins: [react(), tsconfigPaths()],
//   test: {
//     globals: true,
//     environment: 'jsdom',
//     setupFiles: './vitest.setup.mjs',
//   },
// });

export default defineConfig({
  base: "/",
  plugins: [react(), tsconfigPaths()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: './vitest.setup.mjs',
  },
  preview: {
   port: 5173,
   strictPort: true,
  },
  server: {
   port: 5173,
   strictPort: true,
   host: true,
   origin: "http://0.0.0.0:5173",
  },
 });
