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

        /**
 * Exports the actions from the auth slice.
 */
export const { setCredentials, logOut } = authSlice.actions;

        /**
 * Exports the reducer from the auth slice.
 */
export default authSlice.reducer;

/**
 * Selector for getting the current user role from the Redux store.
 * @param {Object} state - The current state of the Redux store.
 * @returns {string|null} The role of the current user, or null if not logged in.
 */
export const selectCurrentRole = (state) => state.auth.role;
/**
 * Selector for getting the current user token from the Redux store.
 * @param {Object} state - The current state of the Redux store.
 * @returns {string|null} The token of the current user, or null if not logged in.
 */
export const selectCurrentToken = (state) => state.auth.token;
/**
 * Selector for getting the current user ID from the Redux store.
 * @param {Object} state - The current state of the Redux store.
 * @returns {string|null} The ID of the current user, or null if not logged in.
 */
export const selectCurrentUserId = (state) => state.auth.userId;
