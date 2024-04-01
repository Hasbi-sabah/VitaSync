import { createSlice } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: {
        userId: null, 
        username: null, 
        token: sessionStorage.getItem('token'),
        role: sessionStorage.getItem('role') },
    reducers: {
        setCredentials: (state, action) => {
            console.log(`SESSION token ${sessionStorage.getItem('token')} , role: ${sessionStorage.getItem('role')}`);
            const {accessToken, userId, role, username} = action.payload;
            console.log(`token ${accessToken}, id: ${userId}, role: ${role}, username: ${username}`);
            
            state.userId = userId;
            state.username = username;
            state.token = accessToken;
            state.role = role;
            sessionStorage.setItem('role', role);
            sessionStorage.setItem('id', userId);
            sessionStorage.setItem('token', accessToken);
        },  
        logOut: (state, action) => {
            state.user = null;
            state.token = null;
            sessionStorage.removeItem('token');
        },
    },
});

export const { setCredentials, logOut } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentRole = (state) => state.auth.role;
export const selectCurrentToken = (state) => state.auth.token;
export const selectCurrentUserId = (state) => state.auth.userId;
export const selectCurrentUsername = (state) => state.auth.username;
