import { createSlice } from "@reduxjs/toolkit";


const authSlice = createSlice({
    name: "auth",
    initialState: {
        userId: null, 
        token: null,
        role: null,
        pinnedIds: [],
    },
    reducers: {
        setCredentials: (state, action) => {
            const {accessToken, userId, role, pinnedIds} = action.payload;
            state.userId = userId;
            state.token = accessToken;
            state.role = role;
            state.pinnedIds = pinnedIds
            localStorage.setItem('role', role);
            localStorage.setItem('id', userId);
            localStorage.setItem('token', accessToken);
            localStorage.setItem('pinnedIds', JSON.stringify(state.pinnedIds)); 
            console.log(state.pinnedIds, localStorage.getItem('pinnedIds'))           
        },  
        logOut: (state, action) => {
            state.userId = null;
            state.token = null;
            state.role = null;
            state.pinnedIds = [];
            localStorage.removeItem('token');
            localStorage.removeItem('id');
            localStorage.removeItem('role');
            localStorage.removeItem('pinnedIds');
        },
        addPinnedId: (state, action) => {
            const { patientId } = action.payload;
            console.log(state.pinnedIds)
            if (!state.pinnedIds.includes(patientId)) {
                state.pinnedIds.push(patientId);
                localStorage.setItem('pinnedIds', JSON.stringify(state.pinnedIds));
            }
        },
        removePinnedId: (state, action) => {
            const { patientId } = action.payload;
            const index = state.pinnedIds.indexOf(patientId);
            if (index !== -1) {
                state.pinnedIds.splice(index, 1);
                localStorage.setItem('pinnedIds', JSON.stringify(state.pinnedIds));
            }
        },
    },
});

export const { setCredentials, logOut, addPinnedId, removePinnedId } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentRole = (state) => state.auth.role;
export const selectCurrentToken = (state) => state.auth.token;
export const selectCurrentUserId = (state) => state.auth.userId;
export const selectPinnedIds = (state) => state.auth.pinnedIds;

