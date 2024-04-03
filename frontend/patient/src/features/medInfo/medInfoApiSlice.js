import { apiSlice } from "../../app/api/apiSlice";

export const MedInfoApiSlice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPatientMedInfoById: builder.query({
            query: (id) => ({
                url: `/api/patient/${id}/info`,
                method: "GET",
            }),
        }),
        addPatientMedInfoById: builder.mutation({
            query: (data) => ({
                url: `/api/patient/${data[0]}/info`,
                method: "POST",
                body: { ...data[1] },
            }),
        }),
        deleteMedInfoById: builder.mutation({
            query: (id) => ({
                url: `/api/med_info/${id}`,
                method: "DELETE",
            }),
        }),
        getMedInfoById: builder.query({
            query: (id) => ({
                url: `/api/med_info/${id}`,
                method: "GET",
            }),
        }),
    }),
});

export const {
    useGetPatientMedInfoByIdQuery,
    useAddPatientMedInfoByIdMutation,
    useDeleteMedInfoByIdMutation,
    useGetMedInfoByIdQuery,
} = MedInfoApiSlice;
