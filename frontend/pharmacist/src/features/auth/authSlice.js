/**
 * Imports the createSlice function from Redux Toolkit.
 * This function is used to generate a slice of the Redux store.
 */
import { createSlice } from "@reduxjs/toolkit";


/**
 * Defines the authSlice by setting up the initial state and reducers.
 * The initial state includes userId, token, and role.
 * Reducers include setCredentials and logOut.
 * @returns {Object} The authSlice object with the defined reducers.
 */
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

/**
 * Exports the actions from the authSlice.
 * These actions can be dispatched to update the state.
 */
export const { setCredentials, logOut } = authSlice.actions;

/**
 * Exports the reducer from the authSlice.
 * This reducer is used to handle state changes.
 */
export default authSlice.reducer;

/**
 * Selectors for accessing the current user's role, token, and user ID from the state.
 */
export const selectCurrentRole = (state) => state.auth.role;
export const selectCurrentToken = (state) => state.auth.token;
export const selectCurrentUserId = (state) => state.auth.userId;
