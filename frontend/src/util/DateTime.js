/* eslint-disable */
export default function formatPostDate(timestamp) {
  const date = new Date(timestamp);
  const month = date.getMonth();
  const day = date.getDate();
  const year = date.getFullYear();
  const now = new Date();
  if (now.getMonth() === month && now.getDate() === day
    && now.getFullYear === year) {
        return date.getTime();
  }
  return month + "/" + day + "/" + year;
}
