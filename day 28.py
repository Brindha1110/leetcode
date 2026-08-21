i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        # Step 2: Search needle in haystack
        h_ptr, n_ptr = 0, 0
        
        while h_ptr < len(haystack):
            if haystack[h_ptr] == needle[n_ptr]:
                h_ptr += 1
                n_ptr += 1
            else:
                if n_ptr == 0:
                    h_ptr += 1
                else:
                    n_ptr = lps[n_ptr - 1]
            
            if n_ptr == len(needle):
                return h_ptr - len(needle)
                
        return -1

        