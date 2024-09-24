import React, { Suspense } from 'react'
const UseRef = React.lazy(()=>import("./UseRef"))

const LazyLoading = () => {
  return (<>
    <h1>lazyLoading</h1>
    <Suspense fallback={<p> Loading </p>}>
        <UseRef/>
    </Suspense>

  </>
  )
}

export default LazyLoading