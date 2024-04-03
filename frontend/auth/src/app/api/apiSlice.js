import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials, logOut } from '../../features/auth/authSlice';

const api = process.env.REACT_APP_API_URL;
const baseQuery = fetchBaseQuery({
    baseUrl: api,
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
