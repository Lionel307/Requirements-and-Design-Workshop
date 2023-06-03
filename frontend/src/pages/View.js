import ViewHeader from '../components/ViewHeader';
import BasicTable from '../components/Table';

import './View.css';

const View = () => {
    return (
    <>
        <ViewHeader /> 
        <h1> My Invoices</h1>
        <div className='viewTable'>
            <BasicTable />   
        </div>		
        
    </>
    )
}

export default View