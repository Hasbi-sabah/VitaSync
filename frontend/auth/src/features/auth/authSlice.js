import { createSlice } from "@reduxjs/toolkit";

/**
 * Authentication Redux slice.
 * 
 * This slice manages the authentication-related state including userId, token, and role.
 */
const authSlice = createSlice({
    name: "auth",
    initialState: {
        userId: null, 
        token: null,
        role: null },
    reducers: {
         /**
         * Reducer for setting user credentials.
         * 
         * @param state - The current state of the slice.
         * @param action - The action containing payload with credentials.
         */
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
        /**
         * Reducer for logging out the user.
         * 
         * @param state - The current state of the slice.
         * @param action - The action (not used in this reducer).
         */
        logOut: (state, action) => {
            state.user = null;
            state.token = null;
            state.id = null;
            localStorage.removeItem('token');
            localStorage.removeItem('id');
            localStorage.removeItem('role');
        },
    },
});

export const { setCredentials, logOut } = authSlice.actions;

export default authSlice.reducer;

/**
 * Selector for retrieving the current role from the state.
 * 
 * @param state - The Redux state.
 * @returns The current role.
 */
export const selectCurrentRole = (state) => state.auth.role;

/**
 * Selector for retrieving the current token from the state.
 * 
 * @param {object} state - The Redux state.
 * @returns {string} The current token.
 */
export const selectCurrentToken = (state) => state.auth.token;

/**
 * Selector for retrieving the current user ID from the state.
 * 
 * @param state - The Redux state.
 * @returns The current user ID.
 */
export const selectCurrentUserId = (state) => state.auth.userId;