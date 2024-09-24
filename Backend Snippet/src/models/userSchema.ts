import { model, Schema } from "mongoose";

const usersSchema: Schema = new Schema({
  username: { type: String },
  Age: { type: Number },
});

const User = model("user",usersSchema)
export default User;
