pub fn prefixes<S: AsRef<str>>(s: S) -> Vec<usize> {
    let s = s.as_ref().chars().collect::<Vec<_>>();
    let mut res = vec![0];

    let mut r = 0;
    let mut l = 0;

    for k in 1..s.len() {
        if k >= r {
            let mut length = 0;
            for i in k..s.len() {
                if s[i] != s[i - k] {
                    break;
                }
                length += 1;
            }
            if length > 0 {
                r = k + length - 1;
                l = k;
                res.push(length);
            } else {
                res.push(0);
            }
        } else {
            let k1 = k - l;
            let b = r - k + 1;
            if res[k1] < b {
                let val = res[k1];
                res.push(val)
            } else {
                let mut length = b;
                for i in r+1..s.len() {
                    if s[i] != s[i - k] { break }
                    length += 1;
                }
                res.push(length);
                r = k + length - 1;
                l = k;
            }
        }
    }

    res
}

pub fn contains(_text: &str, _pattern: &str) -> bool {
    //TODO
    true
}

pub fn is_rotation_of<S: AsRef<str>>(a: S, b: S) -> bool {
    if a.as_ref().len() != b.as_ref().len() {
        return false;
    }
    let double = b.as_ref().to_owned() + b.as_ref();
    return contains(&double, a.as_ref());
}

pub fn is_contained_in_rotation_of<S: AsRef<str>>(a: S, b: S) -> bool {
    if a.as_ref().len() > b.as_ref().len() {
        return false;
    }
    let double = b.as_ref().to_owned() + b.as_ref();
    return contains(&double, a.as_ref())
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn prefixes_works() {
        assert_eq!(prefixes("aaa"), vec![0,2,1]);
        assert_eq!(prefixes("ababab"), vec![0,0,4,0,2,0]);
    }
}
