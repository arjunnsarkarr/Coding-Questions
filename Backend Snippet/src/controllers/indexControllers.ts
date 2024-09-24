import {Request , Response} from "express"

export const home =  async (
    req:Request,
    res:Response
)=>{
    try {
        res.send("Hello Arjun")
    } catch (error) {
        console.log(error)
    }
}