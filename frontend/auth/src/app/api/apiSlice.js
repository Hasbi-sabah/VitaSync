import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials, logOut } from '../../features/auth/authSlice';

const baseQuery = fetchBaseQuery({
    baseUrl: "http://localhost:5000",
    credentials: "include",
    prepareHeaders: (headers, { getState }) => {
        return headers;
    },
})

const baseQueryWithReauth = async (args, api, extraOptions) => {
    let result = await baseQuery(args, api, extraOptions);

    if (result?.error) api.dispatch(logOut());
    return result;
};

export const apiSlice = createApi({
    baseQuery: baseQueryWithReauth,
    endpoints: builder => ({})
})
