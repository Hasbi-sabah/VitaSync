import { createSlice } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: {
        userId: null, 
        token: null,
        role: null },
    reducers: {
        setCredentials: (state, action) => {
            const {accessToken, userId, role} = action.payload;
            state.userId = userId;
            state.token = accessToken;
            state.role = role;
            localStorage.setItem('role', role);
            localStorage.setItem('id', userId);
            localStorage.setItem('token', accessToken);
            console.log(state.userId, state.token, state.role)
        },  
        logOut: (state, action) => {
            state.userId = null;
            state.token = null;
            state.role = null;
            localStorage.removeItem('token');
            localStorage.removeItem('id');
            localStorage.removeItem('role');
        },
    },
});

export const { setCredentials, logOut } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentRole = (state) => state.auth.role;
export const selectCurrentToken = (state) => state.auth.token;
export const selectCurrentUserId = (state) => state.auth.userId;