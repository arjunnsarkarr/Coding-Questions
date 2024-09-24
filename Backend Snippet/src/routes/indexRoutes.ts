import express from "express"
const router = express.Router()
import { home } from "../controllers/indexControllers"

router.get("/",home);



export default router;