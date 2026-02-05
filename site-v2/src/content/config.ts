import { defineCollection, z } from "astro:content";

const pages = defineCollection({
  type: "content",
  schema: z
    .object({
      title: z.string().optional(),
      description: z.string().optional(),
      permalink: z.string().optional(),
      lang: z.string().optional()
    })
    .passthrough()
});

export const collections = {
  pages
};
