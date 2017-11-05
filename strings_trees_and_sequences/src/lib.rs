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
    #[test]
    fn it_works() {
    }
}
