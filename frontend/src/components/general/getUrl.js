export default function getUrl (dev, str) {
  let url = 'http://127.0.0.1:8000' + str
  if (dev) {
    return url
  } else {
    return str
  }
}
