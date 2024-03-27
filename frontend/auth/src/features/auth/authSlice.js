import { createSlice } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: { 
        userId: null, 
        token: localStorage.getItem('token'),
        role: localStorage.getItem('role') },
    reducers: {
        setCredentials: (state, action) => {
            const {accessToken, userId, role} = action.payload;
            state.userId = userId;
            state.token = accessToken;
            state.role = role;
            localStorage.setItem('token', accessToken);
            localStorage.setItem('role', role);
        },
        logOut: (state, action) => {
            state.user = null;
            state.token = null;
            localStorage.removeItem('token');
            localStorage.removeItem('role');
        },
    },
});

export const { setCredentials, logOut } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentUser = (state) => state.auth.userId;
export const selectCurrentToken = (state) => state.auth.token;
export const selectCurrentRole = (state) => state.auth.role;
