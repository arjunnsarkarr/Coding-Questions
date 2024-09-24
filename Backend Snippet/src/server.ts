import express from "express";
const app = express();
import indexRoutes from "./routes/indexRoutes";
import connectDatabase from "./utils/dbConnection";
const PORT = 5500;

app.use("/", indexRoutes);

connectDatabase().then(() => {
  app.listen(PORT, () => {
    console.log(`App is listening on port ${PORT}`);
  });
});
