import lume from "lume/mod.ts";

const site = lume({
  src: "./src",
  dest: "./_site",
  fontsFolder: "/fonts",
});

site.add("/styles.css");

export default site;
