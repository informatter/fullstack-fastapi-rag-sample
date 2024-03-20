
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

[![code format check: prettier](https://img.shields.io/badge/code_format-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

[![js-standard-style](https://img.shields.io/badge/code%20linting-standard-brightgreen.svg)](http://standardjs.com)

![Frontend](https://github.com/informatter/fullstack-fastapi-rag-sample/actions/workflows/frontend_ci_cd.yml/badge.svg?branch=develop)

# Frontend 🚀

This is the general documentation for the frontend and will be updated as the repo progresses.


## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin) to make the TypeScript language service aware of `.vue` types.

If the standalone TypeScript plugin doesn't feel fast enough to you, Volar has also implemented a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669) that is more performant. You can enable it by the following steps:

1. Disable the built-in TypeScript Extension
    1) Run `Extensions: Show Built-in Extensions` from VSCode's command palette
    2) Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
2. Reload the VSCode window by running `Developer: Reload Window` from the command palette.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)

```bash
npm run lint
```

### Check format with [Prettier](https://prettier.io/)
```bash
npm run format-check
```

### Format with [Prettier](https://prettier.io/)

```bash
npm run format
```


### Docker 🐋
If you don't have docker desktop installed, you need to install it:
https://www.docker.com/products/docker-desktop/

**Build the image locally**

Make sure you are in the same directory as the `Dockerfile`, and run:

```bash
    ./build_image.sh
```

Since we are using Vite as the build tool, Vite bakes 🍰 🧑‍🍳 the environment variables when running `vite build` for production. We need to make the local environment variables available to the image when its being built. `build_image.sh` automates all of this process so it does not have to be done manually each time we need to build a new image.

**Run the container**

To run the API service your local environment without using Docker Compose:

```bash
docker run --platform=linux/amd64 -p 5173:80 --rm --name rag-app-local  rag-app:local
```

The wep application is now running at http://localhost:5173


