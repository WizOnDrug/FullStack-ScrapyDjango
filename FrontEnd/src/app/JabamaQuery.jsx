import DivarPage from "../components/templates/DivarPage";



const Jabama = async () => {
  const res = await fetch("http://127.0.0.1:8000/jabama", {
    cache: "no-store",
  });
  const data = await res.json();

  if (data.error) return <h3>مشکلی پیش آمده است</h3>;

  let finalData = data.data;
  return <DivarPage data={data} />;
};

export default Jabama;