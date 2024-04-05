import React, { useMemo } from "react";

export const DOTS = '';

/**
 * Custom hook to generate pagination range based on given parameters.
 * @param totalCount - Total number of items.
 * @param pageSize - Number of items per page.
 * @param sibilingCount - Number of siblings to display.
 * @param currentPage - Current page number.
 * @returns - An array representing the pagination range.
 */
const usePagination = ({
  totalCount,
  pageSize,
  sibilingCount = 1,
  currentPage,
}) => {
    
  const range = (start, end) => {
    const length = end - start + 1;
    return Array.from({ length }, (_, idx) => idx + start);
  }

  const paginationRange = useMemo(() => {
    // Logic
    const totalPageCount = Math.ceil(totalCount / pageSize);

    const totalPageNumbers = sibilingCount + 5;
    
    /*
      Case 1:
      If the number of pages is less than the page numbers we want to show in our paginationComponent, we return the range [1..totalPageCount]
    */
    if (totalPageNumbers >= totalPageCount){
        return range(1, totalPageCount);
    }

    const leftSiblingIndex = Math.max(currentPage - sibilingCount, 1);
    const rightSiblingIndex = Math.min(currentPage + sibilingCount, totalPageCount);

    const shouldShowLeftDots = leftSiblingIndex > 2;
    const shouldShowRightDots = rightSiblingIndex < totalPageCount - 2;

    const firstPageIndex = 1;
    const lastpageIndex = totalPageCount;


    /*
    	Case 2: No left dots to show, but rights dots to be shown
    */
   if (!shouldShowLeftDots && shouldShowRightDots) {
    let leftItemCount = 3 + 2 * sibilingCount;
    let leftRange = range(1, leftItemCount);

    return [...leftRange, DOTS, totalPageCount];
   }


   /*
    	Case 3: No right dots to show, but left dots to be shown
    */
   if (shouldShowLeftDots && !shouldShowRightDots) {
    let rightItemCount = 3 + 2 *sibilingCount;
    let rightRange = range(totalPageCount - rightItemCount + 1, totalPageCount);

    return [firstPageIndex, DOTS, ...rightRange];
   }

    /*
    	Case 4: Both left and right dots to be shown
    */
   if (shouldShowLeftDots && shouldShowRightDots) {
    let middleRange = range(leftSiblingIndex, rightSiblingIndex);

    return [firstPageIndex, DOTS, ...middleRange, DOTS,  lastpageIndex];
   }

  }, [totalCount, pageSize, sibilingCount, currentPage]);


  return paginationRange;
};

export default usePagination;
