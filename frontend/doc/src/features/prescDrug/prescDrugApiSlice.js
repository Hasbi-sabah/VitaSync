import { apiSlice } from "../../app/api/apiSlice";

export const prescDrugApiSclice = apiSlice.injectEndpoints({
    endpoints: builder => ({
        getPrescriptionDrugsById: builder.query({
            query: (id) => ({
                url: `/api/prescription/${id}/drug`,
                method: "GET",
            }),
        }),

        addPrescriptionDrugsById: builder.mutation({
            query: ({id, data}) => ({
                url: `/api/prescription/${id}/drug`,
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json',
                },
            }),
        }),
    }),
});

export const {
    useGetPrescriptionDrugsByIdQuery,
    useAddPrescriptionDrugsByIdMutation,
} = prescDrugApiSclice;
