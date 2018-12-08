class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqEmails = {}
        for string in emails:
            email = ''
            ifPlus = False
            for i, ch in enumerate(string):
                if ch == '+':
                    ifPlus=True
                elif ch != '.' and ifPlus == False:
                    email += ch
                elif ch == '@':
                    email += string[i::]
                    ifPlus=False
                    break
            uniqEmails[email]=True
        return(len(uniqEmails))