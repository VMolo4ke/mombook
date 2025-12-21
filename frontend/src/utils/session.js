import { v4 as uuidv4 } from 'uuid'; 

export const getSessionId = () => {
  let id = localStorage.getItem('x_session_id');
  if (!id) {
    id = uuidv4();
    localStorage.setItem('x_session_id', id);
  }
  return id;
};