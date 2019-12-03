/* Illustration of predefined macros - those which do not
 * need any #include to be in the namespace.
 */

#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    printf("__FILE__: %s\n", __FILE__);
    printf("__DATE__: %s\n", __DATE__);
    printf("__TIME__: %s\n", __TIME__);

    bool cpp = false;
    #if defined(__cplusplus)
    cpp = true;
    #endif
    printf("__cplusplus: %s\n", cpp ? "true" : "false");
    return 0;
}
