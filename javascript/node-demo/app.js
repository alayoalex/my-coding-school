const express = require("express");
const Joi = require("@hapi/joi");
const movies = require("./movies");

const app = express();

app.use(express.json());

app.use("/abc", movies);

app.get("/", (req, res) => {
  res.send("Welcome to Daily Code Buffer in Heroku Auto Deployment!!");
});

const port = process.env.PORT || "5050";
app.listen(port, () => console.log(`Server started on Port ${port}`));
