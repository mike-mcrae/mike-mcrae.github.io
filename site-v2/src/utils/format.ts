export const formatDate = (date: Date) =>
  new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric"
  }).format(date);

export const formatYear = (date: Date) =>
  new Intl.DateTimeFormat("en-US", { year: "numeric" }).format(date);
