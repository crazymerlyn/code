
(defmacro exact [expr]
  (defmacro expand-exact [args]
    (if-let [arg (first args)]
        (cons (macroexpand `(exact ~arg)) (macroexpand `(expand-exact ~(rest args))))
        nil))
  (defn myrationalize [arg]
    `(rationalize ~arg))
  (if (nil? expr)
      nil
      (if (sequential? expr)
          (let [f (first expr)
                args (rest expr)]
            (case f
              + (cons f (map myrationalize (macroexpand `(expand-exact ~args))))
              - (cons f (map myrationalize (macroexpand `(expand-exact ~args))))
              * (cons f (map myrationalize (macroexpand `(expand-exact ~args))))
              / (cons f (map myrationalize (macroexpand `(expand-exact ~args))))
                (cons f (macroexpand `(expand-exact ~args)))))
          expr)))
