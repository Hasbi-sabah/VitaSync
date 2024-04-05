/**
 * This file defines the API slice for the Redux store, using Redux Toolkit Query.
 * It sets up the base query for API requests, including authentication and error handling.
 * The base query uses the fetchBaseQuery utility from Redux Toolkit Query, configured with the API URL and credentials.
 * It also includes a custom query function, baseQueryWithReauth, to handle re-authentication in case of a 401 error.
 * The apiSlice is created using the createApi utility, with the baseQueryWithReauth as the base query.
 * @file
 */

import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials, logOut } from '../../features/auth/authSlice';

/**
 * The API URL is fetched from the environment variables.
 * @type {string}
 */
const apiLink = process.env.REACT_APP_API_URL;

/**
 * The base query for API requests, configured with the API URL, credentials, and a custom header for authorization.
 * @type {BaseQueryFn}
 */
const baseQuery = fetchBaseQuery({
    baseUrl: apiLink,
    credentials: "include",
    prepareHeaders: (headers, { getState }) => {
        const token = localStorage.getItem('token')
        if (token) {
            headers.set("Authorization", `Bearer ${token}`)
        };
        return headers;
    },
})

/**
 * Custom query function to handle re-authentication in case of a 401 error.
 * If a 401 error is caught, it dispatches the logOut action to clear the user's credentials.
 * @param {Object} args - The arguments for the query.
 * @param {Api} api - The API instance.
 * @param {Object} extraOptions - Extra options for the query.
 * @returns {Promise<any>} The result of the query.
 */
const baseQueryWithReauth = async (args, api, extraOptions) => {
    try {
        return await baseQuery(args, api, extraOptions);
    } catch (error) {
        if (error.status === 401) {
            api.dispatch(logOut());
        }
        throw error;
    }
};

/**
 * The API slice, created with createApi, using the baseQueryWithReauth as the base query.
 * It defines the endpoints for the API, which are currently empty.
 * @type {Api}
 */
export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: baseQueryWithReauth,
    endpoints: () => ({}),
});
