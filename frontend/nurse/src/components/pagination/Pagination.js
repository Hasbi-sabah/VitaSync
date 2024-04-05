import React from 'react'
import cn from 'classnames';
import './pagination.css';
import usePagination, { DOTS } from './usePagination';


/**
 * Pagination component for navigating through pages.
 * @param onPageChange - Function to handle page change.
 * @param totalCount - Total number of items.
 * @param siblingCount - Number of siblings to display.
 * @param currentPage - Current page number.
 * @param pageSize - Number of items per page.
 * @param props.className - Additional CSS classes.
 * @returns - The JSX element representing the Pagination component.
 */
const Pagination = ({ 
    onPageChange, 
    totalCount, 
    siblingCount, 
    currentPage,
    pageSize,
    className,
}) => {

    // Generate pagination range
    const paginationRange = usePagination({
        currentPage, 
        totalCount, 
        siblingCount, 
        pageSize,
    });

    // If there are less than 2 in pagination range don't render component
    if (currentPage === 0 || paginationRange.length < 2) {
        return null;
    };

    // Handler for next page
    const onNext = () => {
        onPageChange(currentPage + 1);
    };

    // Handler for previous page
    const onPrevious = () => {
        onPageChange(currentPage - 1);
    };

    // Last page in pagination range
    let lastPage = paginationRange[paginationRange.length - 1];

  return (
    <ul 
        className={cn('pagination-container', className)}>

        {/* Left navigation arrow*/}
        <li 
            className={cn('pagination-item', {disabled: currentPage === 1})} onClick={onPrevious}
        >
            <div className='arrow left' />
        </li>
        {paginationRange.map((pageNumber, index) => {
            if (pageNumber === DOTS) {
                return (
                    <li key={`dots-${index}`} className='pagination-item dots'>
                        &#8230;
                    </li>);
            }
            return(
                <li 
                    key={pageNumber} 
                    className={cn('pagination-item', {selected: pageNumber === currentPage})} onClick={() => onPageChange(pageNumber)}
                >
                    {pageNumber}
                </li>
            );
        })}

        {/*Right Navigation arrow */}
        <li 
            className={cn('pagination-item', {disabled: currentPage === lastPage})} onClick={onNext}
        >
            <div className='arrow right' />
        </li>
    </ul>
  );
};

// Default props
Pagination.defaultProps ={
    siblingCount: 1,
    className: '',
};

export default Pagination