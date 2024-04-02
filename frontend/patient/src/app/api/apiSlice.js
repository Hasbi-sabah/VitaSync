import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials, logOut } from '../../features/auth/authSlice';

const baseQuery = fetchBaseQuery({
    baseUrl: "http://localhost:5000",
    credentials: "include",
    prepareHeaders: (headers, { getState }) => {
        const token = localStorage.getItem('token')
        if (token) {
            headers.set("Authorization", `Bearer ${token}`)
        };
        return headers;
    },
})

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

export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: baseQueryWithReauth,
    endpoints: () => ({}),
});