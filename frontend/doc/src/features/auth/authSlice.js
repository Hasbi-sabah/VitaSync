import { createSlice } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: { 
        user: null, 
        token: localStorage.getItem('token') },
    reducers: {
        setCredentials: (state, action) => {
            const {accessToken, user} = action.payload;
            state.user = user;
            state.token = accessToken;
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

export const selectCurrentUser = (state) => state.auth.user;
export const selectCurrentToken = (state) => state.auth.token;
