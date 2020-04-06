from remerkleable.basic import byte as byte, uint256 as uint256
from remerkleable.core import FixedByteLengthViewHelper as FixedByteLengthViewHelper, View as View, ViewHook as ViewHook, pack_bytes_to_chunks as pack_bytes_to_chunks, zero_node as zero_node
from remerkleable.tree import Gindex as Gindex, Node as Node, PairNode as PairNode, Root as Root, RootNode as RootNode, get_depth as get_depth, subtree_fill_to_contents as subtree_fill_to_contents, subtree_fill_to_length as subtree_fill_to_length, to_gindex as to_gindex
from typing import Any, BinaryIO, Optional, Type, TypeVar

V = TypeVar('V', bound=View)

class RawBytesView(bytes, View):
    def __new__(cls, *args: Any, **kwargs: Any) -> "RawBytesView": ...
    @classmethod
    def default_bytes(cls: Any) -> bytes: ...
    @classmethod
    def coerce_view(cls: Type[V], v: Any) -> V: ...
    @classmethod
    def tree_depth(cls: Any) -> int: ...
    def set_backing(self, value: Any) -> None: ...
    @classmethod
    def decode_bytes(cls: Type[V], bytez: bytes) -> V: ...
    def encode_bytes(self) -> bytes: ...
    def navigate_view(self, key: Any) -> View: ...

class ByteVector(RawBytesView, FixedByteLengthViewHelper, View):
    def __new__(cls, *args: Any, **kwargs: Any) -> "ByteVector": ...
    def __class_getitem__(cls: Any, length: Any) -> Type[ByteVector]: ...
    @classmethod
    def vector_length(cls) -> int: ...
    @classmethod
    def default_bytes(cls: Any) -> bytes: ...
    @classmethod
    def type_repr(cls: Any) -> str: ...
    @classmethod
    def view_from_backing(cls: Type[V], node: Node, hook: Optional[ViewHook[V]]=...) -> V: ...
    def get_backing(self) -> Node: ...
    @classmethod
    def navigate_type(cls: Any, key: Any) -> Type[View]: ...
    @classmethod
    def key_to_static_gindex(cls: Any, key: Any) -> Gindex: ...

Bytes1: Any
Bytes4: Any
Bytes8: Any
Bytes32: Any
Bytes48: Any
Bytes96: Any

class ByteList(RawBytesView, FixedByteLengthViewHelper, View):
    def __new__(cls, *args: Any, **kwargs: Any) -> "ByteList": ...
    def __class_getitem__(cls: Any, limit: Any) -> Type[ByteList]: ...
    @classmethod
    def limit(cls: Any) -> int: ...
    @classmethod
    def default_bytes(cls: Any) -> bytes: ...
    @classmethod
    def type_repr(cls: Any) -> str: ...
    @classmethod
    def view_from_backing(cls: Type[V], node: Node, hook: Optional[ViewHook[V]]=...) -> V: ...
    def get_backing(self) -> Node: ...
    @classmethod
    def contents_depth(cls: Any) -> int: ...
    @classmethod
    def tree_depth(cls: Any) -> int: ...
    @classmethod
    def default_node(cls: Any) -> Node: ...
    @classmethod
    def navigate_type(cls: Any, key: Any) -> Type[View]: ...
    @classmethod
    def key_to_static_gindex(cls: Any, key: Any) -> Gindex: ...
    @classmethod
    def is_fixed_byte_length(cls: Any) -> bool: ...
    @classmethod
    def min_byte_length(cls: Any) -> int: ...
    @classmethod
    def max_byte_length(cls: Any) -> int: ...
    @classmethod
    def deserialize(cls: Type[V], stream: BinaryIO, scope: int) -> V: ...
    def value_byte_length(self) -> int: ...
