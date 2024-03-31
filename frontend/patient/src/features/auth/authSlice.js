import { createSlice } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: {
        userId: null, 
        token: localStorage.getItem('token'),
        role: localStorage.getItem('role') },
    reducers: {
        setCredentials: (state, action) => {
            console.log(`local token ${localStorage.getItem('token')} , role: ${localStorage.getItem('role')}`);
            const {accessToken, userId, role} = action.payload;
            console.log(`token ${accessToken}, id: ${userId}, role: ${role}`);
            
            state.userId = userId;
            state.token = accessToken;
            state.role = role;
            localStorage.setItem('role', role);
            localStorage.setItem('id', userId);
            localStorage.setItem('token', accessToken);
        },  
        logOut: (state, action) => {
            state.user = null;
            state.token = null;
            localStorage.removeItem('token');
        },
    },
});

export const { setCredentials, logOut } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentRole = (state) => state.auth.role;
export const selectCurrentToken = (state) => state.auth.token;
export const selectCurrentUserId = (state) => state.auth.userId;
