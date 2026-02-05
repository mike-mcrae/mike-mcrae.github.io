import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  output: "static",
  trailingSlash: "always",
  integrations: [mdx(), tailwind()],
  markdown: {
    syntaxHighlight: "shiki"
  }
});
